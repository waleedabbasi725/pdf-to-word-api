import os
import tempfile
from pathlib import Path
from pdf2docx import Converter
import gradio as gr

def convert_pdf_to_word(pdf_file):
    """
    Convert PDF to Word with perfect formatting preservation
    """
    try:
        if pdf_file is None:
            raise gr.Error("Please upload a PDF file first!")
        
        # Create temporary directories
        temp_dir = tempfile.mkdtemp()
        
        # Get input PDF path
        pdf_path = pdf_file.name
        
        # Create output Word path
        output_filename = Path(pdf_path).stem + ".docx"
        word_path = os.path.join(temp_dir, output_filename)
        
        # Convert PDF to Word
        print(f"Converting: {pdf_path}")
        cv = Converter(pdf_path)
        cv.convert(word_path, start=0, end=None)
        cv.close()
        
        print(f"✅ Conversion complete: {word_path}")
        
        # Return the Word file path
        return word_path
        
    except Exception as e:
        error_msg = f"❌ Conversion failed: {str(e)}"
        print(error_msg)
        raise gr.Error(error_msg)

# Create Gradio Interface
with gr.Blocks(
    title="PDF to Word Converter",
    theme=gr.themes.Soft(),
    css=".gradio-container {max-width: 900px; margin: auto;}"
) as demo:
    
    gr.Markdown(
        """
        # 📄 PDF to Word Converter API
        
        ### **Perfect conversion with:**
        - ✅ **Color preservation** - All text colors maintained
        - ✅ **Format preservation** - Bold, italic, underline kept
        - ✅ **Image preservation** - All images embedded
        - ✅ **Table preservation** - Tables with borders
        - ✅ **Layout preservation** - Original formatting
        
        ### 🚀 **100% Free | Unlimited Conversions | No Sign-up Required**
        
        ---
        """
    )
    
    with gr.Row():
        with gr.Column(scale=1):
            pdf_input = gr.File(
                label="📤 Upload PDF File",
                file_types=[".pdf"],
                type="filepath",
                file_count="single"
            )
            
            gr.Markdown("**Supported:** Any PDF file (max 50MB)")
            
            convert_btn = gr.Button(
                "🔄 Convert to Word",
                variant="primary",
                size="lg"
            )
        
        with gr.Column(scale=1):
            word_output = gr.File(
                label="📥 Download Word Document",
                type="filepath"
            )
            
            gr.Markdown("**Format:** .docx (Microsoft Word)")
    
    # Status message
    status = gr.Markdown("")
    
    # Connect button to conversion function
    def convert_with_status(pdf):
        status_text = "⏳ **Converting... Please wait...**"
        yield status_text, None
        
        try:
            result = convert_pdf_to_word(pdf)
            success_text = "✅ **Conversion successful! Download your Word file below.**"
            yield success_text, result
        except Exception as e:
            error_text = f"❌ **Error:** {str(e)}"
            yield error_text, None
    
    convert_btn.click(
        fn=convert_with_status,
        inputs=pdf_input,
        outputs=[status, word_output]
    )
    
    gr.Markdown(
        """
        ---
        
        ## 🔌 **API Integration**
        
        ### **For Developers:**
        
        **Use this API in your Android, iOS, or Web app!**
        
        #### **Python Example:**
        ```python
        from gradio_client import Client

        client = Client("YOUR-USERNAME/pdf-to-word-api")
        result = client.predict("document.pdf", api_name="/predict")
        print(f"Converted file: {result}")
        ```
        
        #### **cURL Example:**
        ```bash
        curl -X POST https://YOUR-SPACE-URL.hf.space/api/predict \\
             -F "data=@document.pdf" \\
             -o converted.docx
        ```
        
        #### **JavaScript Example:**
        ```javascript
        const formData = new FormData();
        formData.append('data', pdfFile);
        
        fetch('https://YOUR-SPACE-URL.hf.space/api/predict', {
            method: 'POST',
            body: formData
        }).then(res => res.blob())
          .then(blob => downloadFile(blob, 'converted.docx'));
        ```
        
        ---
        
        ### 📱 **Android Integration**
        
        Complete Android integration code available in the repository.
        
        ### 🛠️ **Tech Stack**
        - Python + Gradio + pdf2docx
        - Hosted on Hugging Face Spaces
        - Open Source (MIT License)
        
        ### 💡 **Credits**
        Built for developers who need reliable PDF to Word conversion.
        
        ---
        
        **Having issues?** Open an issue on GitHub!
        """
    )

# Launch the app
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )
