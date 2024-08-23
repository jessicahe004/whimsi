import React, { useState, useRef } from 'react';
import axios from 'axios';
import './UploadContainer.css';

const UploadContainer: React.FC<{ onCancel: () => void }> = ({ onCancel }) => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [images, setImages] = useState<string[]>([]);
  const [text, setText] = useState<string[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const fileInputRef = useRef<HTMLInputElement | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file && file.type === 'application/pdf') {
      setSelectedFile(file);
    } else {
      alert('Please upload a PDF file.');
    }
  };

  const handleFileUpload = async () => {
    if (selectedFile) {
      const formData = new FormData();
      formData.append('file', selectedFile);
      try {
        const response = await axios.post('http://localhost:8000/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        setImages(response.data.images);
        setText(response.data.text_chunks);
        setCurrentIndex(0);

        alert('File uploaded and images processed successfully.');

        setSelectedFile(null);
        if (fileInputRef.current) {
          fileInputRef.current.value = '';
        }
      } catch (error: any) {
        if (axios.isAxiosError(error)) {
          console.error('Error uploading file:', error.response?.data);
          alert(`Error uploading file: ${error.response?.data?.detail || error.message}`);
        } else {
          console.error('Unexpected error:', error);
          alert('Unexpected error occurred. Please try again.');
        }
      }
    }
  };

  const handleCancelUpload = () => {
    setSelectedFile(null);
    setImages([]);
    setText([]);
    setCurrentIndex(0);
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
    onCancel();
  };

  const goToNext = () => {
    setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
  };

  const goToPrevious = () => {
    setCurrentIndex((prevIndex) => (prevIndex - 1 + images.length) % images.length);
  };

  return (
    <div className="upload-container">
      <input
        type="file"
        accept="application/pdf"
        onChange={handleFileChange}
        ref={fileInputRef}
      />
      {selectedFile && (
        <>
          <button onClick={handleFileUpload}>Confirm Upload</button>
          <button onClick={handleCancelUpload}>Cancel Upload</button>
        </>
      )}
      <div className="slideshow-container">
        {text.length > 0 && images.length > 0 && (
          <>
            <button className="text-button prev" onClick={goToPrevious}>❮</button>
            <div className="text-section">
              <div className="text-content">
                <h3>{`Section ${currentIndex + 1}`}</h3>
                <p>{text[currentIndex]}</p>
              </div>
            </div>
            <div className="image-section">
              <img className="slideshow-image" src={images[currentIndex]} alt={`Generated image ${currentIndex}`} />
            </div>
            <button className="slide-button next" onClick={goToNext}>❯</button>
          </>
        )}
      </div>
    </div>
  );
};

export default UploadContainer;
