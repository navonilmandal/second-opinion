import React, { useState, useRef } from 'react';

interface DocumentDropzoneProps {
  onUploadSuccess: (data: any) => void;
}

export const DocumentDropzone: React.FC<DocumentDropzoneProps> = ({ onUploadSuccess }) => {
  const [isUploading, setIsUploading] = useState(false);
  const [isDragging, setIsDragging] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const processFile = async (file: File) => {
    if (!file.name.endsWith('.pdf') && !file.name.endsWith('.docx')) {
      setError("Please select a PDF or DOCX file.");
      return;
    }

    setError(null);
    setIsUploading(true);

    const formData = new FormData();
    formData.append("file", file);

    const API_URL = import.meta.env.VITE_API_URL || "https://second-opinion-gy3d.onrender.com/api/v1";

    try {
      const uploadRes = await fetch(`${API_URL}/documents/upload`, {
        method: "POST",
        body: formData,
      });

      if (!uploadRes.ok) throw new Error("Upload failed.");
      const uploadData = await uploadRes.json();
      
      const analysisRes = await fetch(`${API_URL}/analysis/analyze`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            document_id: uploadData.document_id,
            provider_id: "hdfc_ergo_seed",
            query: "Identify the major risks, hidden charges, mandatory notification periods, and key exclusions in this insurance policy."
        })
      });
      
      if (!analysisRes.ok) throw new Error("Analysis failed.");
      
      const analysisData = await analysisRes.json();
      onUploadSuccess(analysisData);
      
    } catch (err: any) {
      setError(err.message || "An error occurred.");
    } finally {
      setIsUploading(false);
    }
  };

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) processFile(file);
  };

  const onDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const onDragLeave = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
  };

  const onDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    
    const file = e.dataTransfer.files?.[0];
    if (file) processFile(file);
  };

  return (
    <div 
      className={`upload-dropzone ${isDragging ? 'dragging' : ''}`} 
      onClick={() => fileInputRef.current?.click()}
      onDragOver={onDragOver}
      onDragLeave={onDragLeave}
      onDrop={onDrop}
    >
      <input 
        type="file" 
        ref={fileInputRef} 
        style={{ display: 'none' }} 
        accept=".pdf,.docx" 
        onChange={handleFileSelect}
      />
      <div style={{ marginBottom: '1.5rem', color: isDragging ? 'var(--primary)' : 'var(--text-secondary)' }}>
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
            <polyline points="17 8 12 3 7 8"></polyline>
            <line x1="12" y1="3" x2="12" y2="15"></line>
        </svg>
      </div>
      <h3 style={{ margin: '0 0 0.5rem 0', fontSize: '1.5rem', color: 'var(--text-main)' }}>
        {isDragging ? 'Drop it here!' : 'Drag & Drop your policy document'}
      </h3>
      <p style={{ color: 'var(--text-secondary)', marginBottom: '2rem' }}>
        Supports PDF and DOCX files.
      </p>
      
      {error && <p style={{ color: 'var(--risk-high)', marginBottom: '1rem', fontWeight: '500' }}>{error}</p>}
      
      <button className="btn-primary" disabled={isUploading}>
        {isUploading ? "Extracting & Analyzing with AI..." : "Select File"}
      </button>
    </div>
  );
};
