import ai.onnxruntime.OrtEnvironment
import ai.onnxruntime.OnnxTensor
import java.nio.FloatBuffer
import android.graphics.Bitmap

class SkinCancerClassifier(val context: Context) {

    // 1. Initialize the Environment 
    private val env = OrtEnvironment.getEnvironment()
    
    // 2. Load the model from the Android "assets" folder
    private val session = env.createSession(
        context.assets.open("skin_cancer_mobile_quant.onnx").readBytes()
    )

    fun predict(bitmap: Bitmap): String {
        // --- PREPROCESSING ---

        // Resize image to 224x224 (The size our model expects)
        val resizedBitmap = Bitmap.createScaledBitmap(bitmap, 224, 224, true)
        
        // Create a buffer for (1 batch * 224 height * 224 width * 3 channels)
        val floatBuffer = FloatBuffer.allocate(1 * 224 * 224 * 3)
        
        // Loop through pixels and normalize (0-255 -> Preprocessing)
        for (y in 0 until 224) {
            for (x in 0 until 224) {
                val pixel = resizedBitmap.getPixel(x, y)
                // Extract RGB
                floatBuffer.put((pixel shr 16 and 0xFF).toFloat()) // R
                floatBuffer.put((pixel shr 8 and 0xFF).toFloat())  // G
                floatBuffer.put((pixel and 0xFF).toFloat())        // B
            }
        }
        floatBuffer.rewind()

        // --- INFERENCE ---
        // Create the Input Tensor
        val inputName = session.inputNames.iterator().next()
        val shape = longArrayOf(1, 224, 224, 3)
        val inputTensor = OnnxTensor.createTensor(env, floatBuffer, shape)

        // Run the model
        val result = session.run(mapOf(inputName to inputTensor))
        
        // --- POSTPROCESSING ---
        // Get the output array (Probability for 3 classes)
        val outputTensor = result[0].value as Array<FloatArray>
        val probabilities = outputTensor[0] // Get the first batch result
        
        // Find the index with the highest score
        val maxIndex = probabilities.indices.maxByOrNull { probabilities[it] } ?: -1
        
        return when(maxIndex) {
            0 -> "Benign keratosis"
            1 -> "Melanoma"
            2 -> "Melanocytic nevi"
            else -> "Unknown"
        }
    }
}