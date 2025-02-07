# **🏀 Basketball Shot Tracker**

This project is a **real-time basketball shot tracker** that detects whether a ball goes into the basket or misses. Using **OpenCV** and **NumPy**, it tracks the ball's movement, predicts its trajectory, and determines if the shot is successful.

---

## **📌 Features**
✅ Detects the basketball using color filtering 🎨  
✅ Tracks the ball's movement frame-by-frame 🎥  
✅ Fits a quadratic equation to predict the ball's trajectory 📈  
✅ Determines if the ball lands in the basket 🏀  
✅ Displays **"BASKET"** or **"NO BASKET"** in real-time  

---

## **🔧 Installation**

1️⃣ **Clone the repository**
```bash
git clone https://github.com/yourusername/basketball-shot-tracker.git
cd basketball-shot-tracker
```

2️⃣ **Install dependencies**
```bash
pip install opencv-python numpy
```

3️⃣ **Run the program**
```bash
python shot_tracker.py
```

---

## **📝 How It Works**
1. Loads a **basketball shot video**.
2. Detects the ball using **HSV color filtering**.
3. Tracks the ball's **position** over time.
4. Uses **quadratic fitting** to predict where the ball will land.
5. If the predicted landing position is inside the basket range, it shows **"BASKET"**; otherwise, it shows **"NO BASKET"**.

---

## **🚀 Future Improvements**
✅ Improve accuracy by using **deep learning models** instead of color filtering 🤖  
✅ Detect the basket **automatically** instead of using a fixed range 📌  
✅ Track **multiple basketballs** at once for advanced analysis  
✅ Add a **scoreboard** to count successful shots 🏆  

---
## **👨‍💻 Contributing**
Feel free to **fork this repo**, create a **pull request**, or open an **issue** for suggestions! 🙌

---

