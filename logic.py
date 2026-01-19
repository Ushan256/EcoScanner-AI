import os
import PIL.Image
import numpy as np
from ultralytics import YOLO

class EcoImpact:
    def __init__(self):
        # CO2 saved per kg of recycled material (Global Standards)
        self.factors = {
            'aluminum': 9.1, 
            'plastic': 1.5, 
            'paper': 0.9, 
            'glass': 0.5, 
            'metal': 6.5
        }

    def calculate(self, material, weight_g=25):
        """Calculates CO2 savings based on detected material and average weight."""
        return round((weight_g / 1000) * self.factors.get(material.lower(), 0.1), 4)

class EcoScannerAI:
    def __init__(self):
        # Uses your custom-trained 'best.pt' if found
        weights = 'best.pt' if os.path.exists('best.pt') else 'yolov8s.pt'
        self.model = YOLO(weights) 
        
        # Comprehensive TACO Class Mapping
        # This maps specific labels to general material categories for CO2 math
        self.trash_map = {
            'Aluminium foil': 'aluminum',
            'Bottle': 'plastic',
            'Bottle cap': 'plastic',
            'Can': 'metal',
            'Drink can': 'metal',
            'Carton': 'paper',
            'Cup': 'paper',
            'Glass bottle': 'glass',
            'Plastic bag - wrapper': 'plastic',
            'Plastic container': 'plastic',
            'Straw': 'plastic',
            'Lid': 'plastic',
            'Stylofoam piece': 'plastic',
            'Pop tab': 'metal',
            'Jug': 'plastic',
            'Water bottle': 'plastic'
        }

    def process(self, image_file):
        """Processes an image with logic to correct mislabeled large items."""
        try:
            img = PIL.Image.open(image_file).convert("RGB")
            img_array = np.array(img)
            
            # Use a slightly higher confidence (0.4) to ignore weak 'hallucinations'
            results = self.model.predict(source=img_array, conf=0.4, iou=0.5, save=False)
            
            detections = []
            annotated_img = results[0].plot() 

            for r in results:
                for box in r.boxes:
                    label = self.model.names[int(box.cls[0])]
                    conf = float(box.conf[0])
                    
                    # Calculate box size (width * height)
                    coords = box.xyxy[0] # [x1, y1, x2, y2]
                    width = coords[2] - coords[0]
                    height = coords[3] - coords[1]
                    area = width * height

                    # LOGIC OVERRIDE: If the object is huge but labeled 'Bottle cap', 
                    # it's clearly a jug/container.
                    if label == "Bottle cap" and area > 10000:
                        label = "Plastic container"
                    
                    if label in self.trash_map:
                        detections.append({
                            "label": label, 
                            "material": self.trash_map[label],
                            "confidence": conf
                        })
            return detections, annotated_img
        except Exception as e:
            print(f"Logic Error: {e}")
            return [], None