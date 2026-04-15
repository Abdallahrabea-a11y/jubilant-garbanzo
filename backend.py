import fitz  # PyMuPDF
import os

def analyze_cv(file_path):
    try:
        # قراءة ملف الـ PDF واستخراج النص
        doc = fitz.open(file_path)
        text = "".join([page.get_text() for page in doc])
        doc.close()

        # منطق الـ NLP البسيط لحساب السكور (تقدر تطوره براحتك)
        # بنشوف طول النص ووجود كلمات مفتاحية
        keywords = ["python", "java", "flask", "developer", "engineer", "javascript"]
        score = 0
        found_keywords = []

        for word in keywords:
            if word in text.lower():
                score += 15
                found_keywords.append(word)

        # التأكد إن السكور ميزيدش عن 100
        final_score = min(score + 40, 100) if text else 0
        
        if final_score > 70:
            status = "مقبول مبدئياً"
        else:
            status = "يحتاج لتطوير"

        return f"النتيجة: {status} - السكور: {final_score}% - الكلمات المكتشفة: {', '.join(found_keywords)}"

    except Exception as e:
        return f"خطأ في تحليل الملف: {str(e)}"