import React, { useState } from 'react';

const UploadContainer: React.FC<{ onCancel: () => void }> = ({ onCancel }) => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file && file.type === 'application/pdf') {
      setSelectedFile(file);
    } else {
      alert('Please upload a PDF file.');
    }
  };

  const handleFileUpload = () => {
    if (selectedFile) {
      // Handle the file upload logic here
      console.log('Uploading file:', selectedFile);
      // Reset the file input after upload
      setSelectedFile(null);
    }
  };

  const handleCancelUpload = () => {
    setSelectedFile(null);
    onCancel();
  };

  return (
    <div className="upload-container">
      <input type="file" accept="application/pdf" onChange={handleFileChange} />
      {selectedFile && (
        <>
          <button onClick={handleFileUpload}>Confirm Upload</button>
          <button onClick={handleCancelUpload}>Cancel Upload</button>
        </>
      )}
    </div>
  );
};

export default UploadContainer;
