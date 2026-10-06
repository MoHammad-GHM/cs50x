# QuickMood Mini

#### Video Demo:
https://youtu.be/HgMRAIQ3LSE

---

## 👤 Author
- **Name:** MoHammad  
- **edX Username:** MG_2507_FWWP 
- **GitHub Username:** MoHammad-GHM
- **City/Country:** Iran , alborz , karaj
- **Date Recorded:** 2025 dec 29
 —

## 📌 Project Title
**QuickMood Mini – A Simple Daily Mood Tracker**

---

## 📖 Description

یک اپلیکیشن iOS سبک، سریع و کاربرپسند است که به کاربران اجازه می‌دهد حالات روحی روزانه خود را با استفاده از ایموجی و یادداشت ثبت کنند. هدف این پروژه ایجاد یک ابزار ساده اما کاربردی برای پیگیری احساسات روزانه است؛ ابزاری که بتواند در چند ثانیه حالت روحی را ذخیره کند و در آینده امکان مرور و تحلیل آن را فراهم سازد.

این اپلیکیشن با استفاده از **SwiftUI** طراحی شده و داده‌ها را به کمک **UserDefaults** ذخیره می‌کند. ساختار پروژه شامل یک مدل داده‌ای ساده، یک سیستم ذخیره‌سازی محلی، و چندین ویوی SwiftUI است که تجربه‌ای روان و مدرن ارائه می‌دهند. همچنین برای افزایش کیفیت تجربه کاربری، از انیمیشن‌های نرم، طراحی مینیمال و دسته‌بندی هوشمند داده‌ها استفاده شده است.

---

## ✨ Features

- انتخاب سریع ایموجی برای ثبت حالت روحی (😊 😐 😞 😡 😴)
- امکان افزودن یادداشت برای هر حالت
- ذخیره‌سازی محلی با UserDefaults و Codable
- نمایش تاریخچه حالات به صورت:
  - گروه‌بندی روزانه (جدیدترین ابتدا)
  - دسته‌بندی بر اساس ایموجی
- انیمیشن ذخیره‌سازی ("✨ Mood saved!")
- طراحی مدرن با SwiftUI و گرادیان پس‌زمینه
- تست‌های پایه برای Unit Test و UI Test

---

## 🧩 Project Structure

### **1. ContentView.swift**
این فایل هسته اصلی اپلیکیشن است و شامل بخش‌های زیر می‌شود:

#### **Model**
- ساختار `Mood` شامل:
  - شناسه یکتا (UUID)
  - تاریخ
  - زمان
  - ایموجی
  - یادداشت
- قابل سریال‌سازی با `Codable`

#### **MoodStorage**
- مدیریت ذخیره‌سازی داده‌ها
- ذخیره و بارگذاری از UserDefaults
- مرتب‌سازی داده‌ها بر اساس تاریخ
- گروه‌بندی داده‌ها بر اساس روز
- فیلتر کردن حالات بر اساس ایموجی

#### **UI Components**
- انتخاب ایموجی
- نمایش پیام انیمیشنی ذخیره‌سازی
- نمایش تاریخچه روزانه
- نمایش تاریخچه بر اساس ایموجی
- ویوهای کمکی:
  - `DaySectionView`
  - `MoodDetailView`
  - `MoodCategoryView`

---

### **2. QuickMood_MiniApp.swift**
- نقطه شروع اپلیکیشن با annotation `@main`
- بارگذاری ContentView
- پیکربندی ModelContainer (در صورت نیاز به توسعه آینده)

---

### **3. QuickMood_MiniTests.swift**
- تست‌های پایه برای بررسی عملکرد بخش‌های مختلف
- آماده برای توسعه تست‌های بیشتر

---

### **4. QuickMood_MiniUITests.swift**
- تست رابط کاربری
- بررسی عملکرد لانچ اپلیکیشن
- تست تعاملات پایه

---

### **5. QuickMood_MiniUITestsLaunchTests.swift**
- تست مخصوص صفحه لانچ
- ثبت اسکرین‌شات اولیه اپلیکیشن

---

## 🛠 Technical Details

- **Language:** Swift  
- **Framework:** SwiftUI  
- **Storage:** UserDefaults + Codable  
- **Architecture:** MVVM ساده  
- **Animations:** Spring animations  
- **Testing:** XCTest + Testing framework  

---

## 🎨 Design Choices

- استفاده از ایموجی‌ها برای ثبت سریع و جهانی احساسات
- طراحی مینیمال و تمیز با گرادیان ملایم
- استفاده از کارت‌های سفید با سایه نرم برای خوانایی بهتر
- نمایش تاریخچه به صورت گروه‌بندی‌شده برای مرور آسان
- استفاده از انیمیشن‌های Spring برای حس طبیعی‌تر تعاملات

---

## 🚀 How to Run

1. پروژه را در Xcode باز کنید  
2. اپلیکیشن را روی شبیه‌ساز iOS یا دستگاه واقعی اجرا کنید  
3. با انتخاب ایموجی، حالت روحی خود را ثبت کنید  
4. یادداشت اضافه کنید و ذخیره کنید  
5. تاریخچه را در بخش‌های مختلف مشاهده کنید  

---

## 📌 Future Improvements

- اضافه کردن نمودارهای آماری برای تحلیل حالات روحی
- همگام‌سازی داده‌ها با iCloud
- افزودن ویجت‌های iOS برای ثبت سریع‌تر
- اضافه کردن قابلیت ویرایش یا حذف رکوردها
- اضافه کردن تم‌های رنگی مختلف

---




## 📌 Project Title
**QuickMood Mini – A Simple Daily Mood Tracker**

---

## 📖 Description

QuickMood Mini is a lightweight, fast, and user‑friendly iOS application that allows users to record their daily moods using emojis and optional notes. The goal of this project is to create a simple yet practical tool for tracking emotional states throughout the day—something that can be used in just a few seconds and later reviewed to reflect on emotional patterns.

The app is built using **SwiftUI**, and it stores data locally using **UserDefaults**. The project includes a clean data model, a local storage manager, and multiple SwiftUI views that together create a smooth and modern user experience. To enhance usability, the app uses soft animations, a minimalistic design, and smart grouping of mood entries.

---

## ✨ Features

- Quick emoji selection for mood logging (😊 😐 😞 😡 😴)
- Add a note to each mood entry
- Local storage using UserDefaults + Codable
- Mood history displayed in two formats:
  - Grouped by day (newest first)
  - Filtered by emoji category
- Animated “✨ Mood saved!” confirmation
- Modern SwiftUI interface with gradient background
- Basic Unit Tests and UI Tests included

---

## 🧩 Project Structure

### **1. ContentView.swift**
This is the core of the application and includes:

#### **Model**
- `Mood` struct containing:
  - UUID identifier  
  - Date  
  - Time  
  - Emoji  
  - Note  
- Conforms to `Codable` for easy serialization

#### **MoodStorage**
- Handles saving and loading mood entries
- Uses UserDefaults for persistent storage
- Sorts entries by date
- Groups moods by day
- Filters moods by emoji

#### **UI Components**
- Emoji selection interface
- Animated save message
- Daily mood history
- Emoji‑based mood history
- Supporting views:
  - `DaySectionView`
  - `MoodDetailView`
  - `MoodCategoryView`

---

### **2. QuickMood_MiniApp.swift**
- App entry point using `@main`
- Loads `ContentView` as the main interface
- Prepares a ModelContainer (for potential future expansion)

---

### **3. QuickMood_MiniTests.swift**
- Basic unit test file
- Ready for adding more detailed tests

---

### **4. QuickMood_MiniUITests.swift**
- UI test suite
- Verifies app launch and basic interactions

---

### **5. QuickMood_MiniUITestsLaunchTests.swift**
- Launch screen test
- Captures an initial screenshot of the app

---

## 🛠 Technical Details

- **Language:** Swift  
- **Framework:** SwiftUI  
- **Storage:** UserDefaults + Codable  
- **Architecture:** Simple MVVM  
- **Animations:** Spring animations  
- **Testing:** XCTest + Testing framework  

---

## 🎨 Design Choices

- Emojis used as a universal, fast way to express emotions
- Clean, minimal UI with soft gradient background
- White cards with subtle shadows for readability
- Grouped history for easier navigation
- Smooth spring animations for natural interactions

---

## 🚀 How to Run

1. Open the project in Xcode  
2. Run the app on an iOS simulator or a real device  
3. Select an emoji to log your mood  
4. Add a note and save  
5. View your mood history in the main list or by emoji category  

---

## 📌 Future Improvements

- Add charts to visualize mood trends over time  
- Sync data with iCloud  
- Add iOS widgets for faster mood logging  
- Add editing and deleting mood entries  
- Add multiple color themes  

---
