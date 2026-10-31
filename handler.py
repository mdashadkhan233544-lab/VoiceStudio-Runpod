import runpod

def handler(job):
    # ইউজার থেকে ইনপুট রিসিভ করা
    job_input = job["input"]
    text_to_speak = job_input.get("text", "হ্যালো, এটি একটি টেস্ট ভয়েস।")
    
    # [পরবর্তীতে এখানে VoiceStudio এর আসল কোড যুক্ত করা হবে যা অডিও তৈরি করবে]
    
    print(f"Received task to generate voice for: {text_to_speak}")
    
    # আউটপুট ফেরত পাঠানো
    return {
        "status": "success", 
        "message": "Serverless backend is working!",
        "received_text": text_to_speak
    }

# রানপড সার্ভারলেস স্টার্ট করা
runpod.serverless.start({"handler": handler})