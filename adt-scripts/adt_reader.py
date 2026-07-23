import json
import os

def load_uuid_map(root_path="."):
    """قراءة ملف الفهرس المركزي uuidMap.json من الجذر"""
    map_file = os.path.join(root_path, "uuidMap.json")
    
    if not os.path.exists(map_file):
        print(f"[!] تحذير: ملف uuidMap.json غير موجود في المسار: {map_file}")
        return {}
    
    with open(map_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        print("[+] تم قراءة الفهرس المركزي بنجاح.")
        return data

def read_component_metadata(json_file_path):
    """قراءة ملف الميتافيتا الخاص بكل مكون (مثل lab_1.json أو metadata.json)"""
    if not os.path.exists(json_file_path):
        print(f"[!] ملف الميتافيتا غير موجود: {json_file_path}")
        return None
        
    with open(json_file_path, 'r', encoding='utf-8') as f:
        metadata = json.load(f)
        return metadata

def main():
    # 1. تحميل الخريطة المركزية للمكونات
    uuid_map = load_uuid_map()
    
    if not uuid_map:
        return

    print("\n--- تفاصيل المكونات المسجلة في النظام ---")
    
    # 2. المرور على كل مكون ومساره حسب الـ UUID الخاص به
    for uuid_key, component_info in uuid_map.items():
        print(f"\nUUID: {uuid_key}")
        print(f"Component Info: {component_info}")
        
        # لو متاح مسار لملف ميتافيتا خاص بالمكون، نقوم بقراءته
        if isinstance(component_info, dict) and "path" in component_info:
            meta_path = component_info["path"]
            meta_data = read_component_metadata(meta_path)
            if meta_data:
                print(f"   -> Loaded Metadata: {meta_data}")

if __name__ == "__main__":
    main()
