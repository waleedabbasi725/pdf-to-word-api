# 📄 PDF to Word Converter API

**Free, unlimited PDF to Word conversion with perfect formatting preservation.**

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/YOUR-USERNAME/pdf-to-word-api)
[![GitHub](https://img.shields.io/github/stars/YOUR-USERNAME/pdf-to-word-api?style=social)](https://github.com/YOUR-USERNAME/pdf-to-word-api)

---

## 🚀 **Live Demo**

Try it now: **[Launch Converter](https://huggingface.co/spaces/YOUR-USERNAME/pdf-to-word-api)**

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

client = Client("YOUR-USERNAME/pdf-to-word-api")
result = client.predict("document.pdf", api_name="/predict")
print(f"Converted: {result}")
