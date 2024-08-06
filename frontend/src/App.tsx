import React, { useState } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import Book from './Book';
import UploadContainer from './UploadContainer';
import './App.css';

const App: React.FC = () => {
  const [showUploadContainer, setShowUploadContainer] = useState(false);

  const toggleUploadContainer = () => {
    setShowUploadContainer((prev) => !prev);
  };

  const handleCancelUpload = () => {
    setShowUploadContainer(false);
  };

  return (
    <div className="App">
      <h1>whimsi</h1>
      <button onClick={toggleUploadContainer}>
        {showUploadContainer ? 'Close Upload' : 'Upload PDF'}
      </button>
      {showUploadContainer && <UploadContainer onCancel={handleCancelUpload} />}
      <Canvas>
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} />
        <Book />
        <OrbitControls />
      </Canvas>
    </div>
  );
};

export default App;
