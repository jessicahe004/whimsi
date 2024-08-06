import React, { useRef, useState } from 'react';
import { useGLTF, Html } from '@react-three/drei';
import { useFrame } from '@react-three/fiber';
import * as THREE from 'three';
import './Book.css';

const Book = () => {
  const group = useRef<THREE.Group>(null!);
  const { nodes, isLoading } = useGLTF('/book.gltf') as any;
  const totalPages = 19; 

  const pageMaterial = new THREE.MeshStandardMaterial({
    color: 'beige',
    opacity: 1,
    transparent: true,
  });

  if (isLoading) {
    return (
      <Html center>
        <div>Loading...</div>
      </Html>
    );
  }

  return (
    <group
      ref={group}
      dispose={null}
    >
      {[...Array(totalPages)].map((_, index) => {
        const meshKey = `mesh_${index}`; 
        return (
          <mesh
            key={meshKey}
            geometry={nodes[meshKey]?.geometry}
            material={pageMaterial} 
            visible={true} 
          />
        );
      })}
    </group>
  );
};

export default Book;
