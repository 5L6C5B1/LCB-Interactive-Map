"""
Automatically embed external tilesets into TMX files
This script will:
1. Find all TMX files
2. Look for external tileset references (<tileset source="...">)
3. Embed the tileset data directly into the TMX file
"""

import xml.etree.ElementTree as ET
import os
from pathlib import Path

def embed_tilesets_in_tmx(tmx_path):
    """Embed external tilesets into a TMX file"""
    print(f"\nProcessing: {tmx_path}")
    
    try:
        tree = ET.parse(tmx_path)
        root = tree.getroot()
        
        modified = False
        tmx_dir = os.path.dirname(tmx_path)
        
        # Find all tileset elements
        for tileset in root.findall('tileset'):
            source = tileset.get('source')
            
            if source:
                # External tileset found
                print(f"  Found external tileset: {source}")
                
                # Resolve the tileset path
                tsx_path = os.path.join(tmx_dir, source)
                tsx_path = os.path.normpath(tsx_path)
                
                if not os.path.exists(tsx_path):
                    print(f"  ⚠️ Warning: Tileset file not found: {tsx_path}")
                    continue
                
                # Parse the external tileset
                try:
                    tsx_tree = ET.parse(tsx_path)
                    tsx_root = tsx_tree.getroot()
                    
                    # Copy attributes from external tileset
                    firstgid = tileset.get('firstgid')
                    
                    # Copy all attributes from tsx_root to tileset
                    for key, value in tsx_root.attrib.items():
                        tileset.set(key, value)
                    
                    # Restore firstgid (it's specific to the map)
                    tileset.set('firstgid', firstgid)
                    
                    # Remove the 'source' attribute
                    del tileset.attrib['source']
                    
                    # Copy all child elements from external tileset
                    for child in tsx_root:
                        tileset.append(child)
                    
                    print(f"  ✅ Embedded tileset: {tileset.get('name', 'unnamed')}")
                    modified = True
                    
                except Exception as e:
                    print(f"  ❌ Error parsing tileset {tsx_path}: {e}")
                    continue
        
        if modified:
            # Save the modified TMX file
            # Make a backup first
            backup_path = str(tmx_path) + '.backup'
            if not os.path.exists(backup_path):
                import shutil
                shutil.copy2(tmx_path, backup_path)
                print(f"  💾 Backup created: {backup_path}")
            
            # Write the modified file
            tree.write(tmx_path, encoding='utf-8', xml_declaration=True)
            print(f"  ✅ File updated successfully!")
            return True
        else:
            print(f"  ℹ️ No external tilesets found (already embedded?)")
            return False
            
    except Exception as e:
        print(f"  ❌ Error processing file: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Process all TMX files in the data/maps directory"""
    maps_dir = Path('data/maps')
    
    if not maps_dir.exists():
        print(f"❌ Maps directory not found: {maps_dir}")
        return
    
    print("=" * 60)
    print("TMX Tileset Embedding Tool")
    print("=" * 60)
    print(f"\nSearching for TMX files in: {maps_dir.absolute()}")
    
    tmx_files = list(maps_dir.glob('*.tmx'))
    
    if not tmx_files:
        print("❌ No TMX files found!")
        return
    
    print(f"\nFound {len(tmx_files)} TMX files")
    
    # Ask for confirmation
    print("\n⚠️ This will modify your TMX files (backups will be created)")
    response = input("Continue? (yes/no): ").strip().lower()
    
    if response not in ['yes', 'y']:
        print("❌ Cancelled by user")
        return
    
    # Process all files
    success_count = 0
    for tmx_file in tmx_files:
        if embed_tilesets_in_tmx(tmx_file):
            success_count += 1
    
    print("\n" + "=" * 60)
    print(f"✅ Complete! {success_count}/{len(tmx_files)} files modified")
    print("=" * 60)
    print("\n💡 Tip: If something went wrong, restore from .backup files")

if __name__ == '__main__':
    main()