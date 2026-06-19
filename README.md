# 🧚 Pixie-Trixie
## Image Encryption & Decryption Tool • Python GUI

![Python](https://img.shields.io/badge/PYTHON-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white) ![Library](https://img.shields.io/badge/LIBRARY-PILLOW-orange?style=for-the-badge) ![Security](https://img.shields.io/badge/SECURITY-PIXEL%20SCRAMBLING-cyan?style=for-the-badge)

## 📖 Overview
Pixie-Trixie is a specialized cybersecurity utility developed during my internship at Prodigy Infotech. It provides a robust yet user-friendly way to secure image data through advanced pixel manipulation. By combining Seeded Shuffling and Bitwise XOR operations, it transforms any standard image into unreadable digital static.

## ✨ Key Features
- **Secure Pixel Scrambling:** Physically rearranges pixel coordinates based on a private key.
- **Dual-Layer Encryption:** Applies bitwise XOR color shifting in addition to spatial shuffling.
- **Zero Loss Decryption:** Uses lossless processing to ensure images are restored with 100% original quality.
- **Animated Terminal UI:** Features a centered, responsive dashboard with a winking "Pixie" guardian.
- **Cross-Platform GUI:** Integrated file dialogs for easy image and folder selection.

## 🛠️ How It Works
| Step | Action | Logic / Formula |
| :--- | :--- | :--- |
| **01** | **Load Matrix** | Image is converted into a raw RGB pixel array. |
| **02** | **Seeded Shuffle** | `random.seed(key)` ensures the shuffle is unique but reproducible. |
| **03** | **XOR Shift** | Every pixel value $P$ is transformed: $P' = P \oplus (\text{key} \pmod{255})$. |

## 🚀 Installation & Usage

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/Mohammedshezil/PRODIGY_CS_02.git](https://github.com/Mohammedshezil/PRODIGY_CS_02.git)
   cd PRODIGY_CS_02
2 **Install Dependencies:**
  ```bash
  pip install -r requirements.txt
