import torch
from utils.model import ResNet9 

# 1. Define your disease classes count based on your app.py
disease_classes_count = 38
disease_model = ResNet9(3, disease_classes_count)

# 2. Load your current PyTorch weights
disease_model_path = 'models/plant_disease_model.pth'
disease_model.load_state_dict(torch.load(disease_model_path, map_location=torch.device('cpu')))
disease_model.eval()

# 3. Create a dummy image tensor (1 batch, 3 color channels, 256x256 size) to trace the model
dummy_input = torch.randn(1, 3, 256, 256)

# 4. Export to ONNX
onnx_model_path = "models/plant_disease_model.onnx"
print("Converting model to ONNX... Please wait.")

torch.onnx.export(
    disease_model, 
    dummy_input, 
    onnx_model_path, 
    export_params=True, 
    opset_version=11, 
    do_constant_folding=True,
    input_names=['input'], 
    output_names=['output']
)

print(f"Success! Model successfully saved at: {onnx_model_path}")