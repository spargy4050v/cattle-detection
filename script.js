const imageInput = document.getElementById("imageInput");
const previewContainer = document.getElementById("previewContainer");
const previewImage = document.getElementById("previewImage");
const predictBtn = document.getElementById("predictBtn");
const loading = document.getElementById("loading");
const result = document.getElementById("result");
const prediction = document.getElementById("prediction");
const confidence = document.getElementById("confidence");
const errorBox = document.getElementById("error");

const uploadTab = document.getElementById("uploadTab");
const cameraTab = document.getElementById("cameraTab");
const uploadSection = document.getElementById("uploadSection");
const cameraSection = document.getElementById("cameraSection");
const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const captureBtn = document.getElementById("captureBtn");

let capturedBlob = null; // holds image blob from camera

// Tab switching
uploadTab.addEventListener("click", () => {
  uploadTab.classList.add("active");
  cameraTab.classList.remove("active");
  uploadSection.classList.remove("hidden");
  cameraSection.classList.add("hidden");
  stopCamera();
});

cameraTab.addEventListener("click", async () => {
  cameraTab.classList.add("active");
  uploadTab.classList.remove("active");
  cameraSection.classList.remove("hidden");
  uploadSection.classList.add("hidden");
  startCamera();
});

// Show image preview (upload)
imageInput.addEventListener("change", () => {
  const file = imageInput.files[0];
  if (file) {
    capturedBlob = null;
    previewContainer.classList.remove("hidden");
    previewImage.src = URL.createObjectURL(file);
  } else {
    previewContainer.classList.add("hidden");
    previewImage.src = "";
  }
});

// Capture image from camera
captureBtn.addEventListener("click", () => {
  const context = canvas.getContext("2d");
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  canvas.toBlob(blob => {
    capturedBlob = blob;
    previewContainer.classList.remove("hidden");
    previewImage.src = URL.createObjectURL(blob);
  }, "image/jpeg");
});

// Predict button
predictBtn.addEventListener("click", async () => {
  let file = imageInput.files[0];
  if (!file && capturedBlob) {
    file = new File([capturedBlob], "capture.jpg", { type: "image/jpeg" });
  }

  if (!file) {
    showError("Please upload or capture a photo first.");
    return;
  }

  result.classList.add("hidden");
  errorBox.classList.add("hidden");
  loading.classList.remove("hidden");

  try {
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://127.0.0.1:8000/predict_breed", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }

    if (!response || !response.ok) {
      throw lastError || new Error("All API endpoints failed");
    }

    const data = await response.json();
    if (!data.prediction || data.confidence === undefined) {
      throw new Error("Invalid response format from server.");
    }

    prediction.textContent = data.prediction;
    confidence.textContent = (data.confidence * 100).toFixed(2) + "%";
    result.classList.remove("hidden");
  } catch (err) {
    console.error(err);
    showError("Failed to get prediction. Please check if backend is running.");
  } finally {
    loading.classList.add("hidden");
  }
});

// Helper functions
function showError(message) {
  errorBox.textContent = message;
  errorBox.classList.remove("hidden");
}

async function startCamera() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } });
    video.srcObject = stream;
  } catch (err) {
    showError("Could not access camera. Please allow permissions.");
    console.error(err);
  }
}

function stopCamera() {
  const stream = video.srcObject;
  if (stream) {
    stream.getTracks().forEach(track => track.stop());
    video.srcObject = null;
  }
}
