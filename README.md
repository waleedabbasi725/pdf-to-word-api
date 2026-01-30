# 📄 PDF to Word Converter API

**Free, unlimited PDF to Word conversion with perfect formatting preservation.**

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/waleedabbasi725/pdf-to-word-api)
[![GitHub](https://img.shields.io/github/stars/waleedabbasi725/pdf-to-word-api?style=social)](https://github.com/waleedabbasi725/pdf-to-word-api)

---

## 🚀 **Live Demo**

Try it now: **[Launch Converter](https://huggingface.co/spaces/waleedabbasi725/pdf-to-word-api)**

---

## ✨ **Features**

- ✅ **Perfect Color Preservation** - RGB, CMYK, all formats
- ✅ **Format Preservation** - Bold, italic, underline, fonts
- ✅ **Image Preservation** - All images embedded
- ✅ **Table Preservation** - Tables with borders
- ✅ **Layout Preservation** - Original document structure
- ✅ **100% Free** - No API keys, no limits
- ✅ **Fast Conversion** - Typical file in 5-10 seconds
- ✅ **Secure** - Files auto-deleted after conversion

---

## 🔌 **API Usage**

### **Python**

```python
from gradio_client import Client

client = Client("waleedabbasi725/pdf-to-word-api")
result = client.predict("document.pdf", api_name="/predict")
print(f"Converted: {result}")
```
### **cURL**
```bash
curl -X POST https://waleedabbasi725-pdf-to-word-api.hf.space/api/predict \
     -F "data=@document.pdf" \
     -o converted.docx
```
### **JavaScript**
```javascript
const formData = new FormData();
formData.append('data', pdfFile);

fetch('https://waleedabbasi725-pdf-to-word-api.hf.space/api/predict', {
    method: 'POST',
    body: formData
})
.then(res => res.blob())
.then(blob => {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'converted.docx';
    a.click();
});
```
### ** Local Development**
```bash
git clone https://github.com/waleedabbasi725/pdf-to-word-api.git
cd pdf-to-word-api
pip install -r requirements.txt
python app.py
```

---

## 📱 **Android Integration**

Complete Android Kotlin code available in repository.

---

## 📊 **Performance**

- **Small PDFs (< 5MB):** 3-5 seconds
- **Medium PDFs (5-20MB):** 5-15 seconds
- **Large PDFs (20-50MB):** 15-30 seconds

---

## 📄 **License**

MIT License - Use freely in your projects!

---

**⭐ If this helped you, please star the repo!**
