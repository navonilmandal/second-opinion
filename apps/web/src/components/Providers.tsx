import React from 'react';

interface ProvidersProps {
  onBack: () => void;
}

export const Providers: React.FC<ProvidersProps> = ({ onBack }) => {
  const companies = [
    "Tata AIG General Insurance",
    "HDFC Ergo General Insurance",
    "ICICI Lombard General Insurance",
    "New India Assurance",
    "United India Insurance",
    "National Insurance",
    "Star Health and Allied Insurance",
    "Bajaj Allianz General Insurance",
    "SBI General Insurance",
    "Care Health Insurance"
  ];

  return (
    <div className="fade-in" style={{ maxWidth: '1000px', margin: '0 auto', padding: '0 2rem' }}>
      <button 
        className="btn-outline" 
        onClick={onBack}
        style={{ marginBottom: '2rem' }}
      >
        &larr; Back to Home
      </button>
      
      <div className="glass-panel" style={{ padding: '3rem' }}>
        <h2 style={{ fontSize: '2.5rem', marginBottom: '1rem', color: 'var(--text-main)' }}>
          Supported Providers
        </h2>
        <p style={{ color: 'var(--text-secondary)', fontSize: '1.2rem', marginBottom: '2rem' }}>
          Our AI engine is currently trained and benchmarked to extract, analyze, and score policies from the following insurance companies:
        </p>
        
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '1.5rem' }}>
          {companies.map((company, index) => (
            <div 
              key={index} 
              style={{ 
                padding: '1.5rem', 
                border: '1px solid var(--border)', 
                borderRadius: '12px',
                background: 'rgba(139, 92, 246, 0.03)',
                fontWeight: '600',
                color: 'var(--primary)',
                display: 'flex',
                alignItems: 'center',
                boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.02)'
              }}
            >
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ marginRight: '12px', color: 'var(--risk-low)' }}>
                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                <polyline points="22 4 12 14.01 9 11.01"></polyline>
              </svg>
              {company}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
