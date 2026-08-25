import React, { useState } from 'react';
import './index.css';
import { DocumentDropzone } from './components/upload/DocumentDropzone';
import { PolicyScoreCard } from './components/scores/PolicyScoreCard';
import { Providers } from './components/Providers';

const App: React.FC = () => {
  const [result, setResult] = useState<any>(null);
  const [showProviders, setShowProviders] = useState(false);

  return (
    <div className="layout-container">
      {/* Top Navigation */}
      <nav className="navbar">
        <div className="logo-container" style={{ cursor: 'pointer' }} onClick={() => setShowProviders(false)}>
          <div className="logo-icon">2</div>
          <span className="logo-text">Second Opinion</span>
        </div>
        <a
          href="https://github.com/navonilmandal/second-opinion/releases/latest"
          target="_blank"
          rel="noopener noreferrer"
          className="btn-outline"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ marginRight: '8px' }}>
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
            <polyline points="7 10 12 15 17 10"></polyline>
            <line x1="12" y1="15" x2="12" y2="3"></line>
          </svg>
          Download Extension
        </a>
      </nav>

      {showProviders ? (
        <Providers onBack={() => setShowProviders(false)} />
      ) : (
        <>
          <header className="hero-section fade-in">
            <h1 className="hero-title interactive-hero">
              Want To Get a{' '}
              <span className="typewriter-second">
                <span className="gradient-text">Second&nbsp;</span>
              </span>
              <span className="falling-word-container">
                <span className="gradient-text falling-word">Opinion</span>
                <div className="rescue-bot">
                  <svg className="minecraft-steve" width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <g className="steve-pickaxe-anim">
                      <g transform="translate(26, -10) rotate(15)">
                        <rect x="14" y="16" width="4" height="36" fill="#8b5a2b" transform="rotate(45, 16, 34)" />
                        <path d="M-4 12 Q 16 -4 36 12 L 30 18 Q 16 6 2 18 Z" fill="#33ebcb" transform="rotate(45, 16, 34)" />
                      </g>
                    </g>
                    <g transform="translate(42, 26) rotate(-150)">
                      <rect x="-4" y="0" width="8" height="24" fill="#f1b48b" />
                      <rect x="-4" y="0" width="8" height="12" fill="#00aaaa" />
                    </g>
                    <rect x="22" y="42" width="8" height="22" fill="#2b2b84" />
                    <rect x="20" y="18" width="16" height="24" fill="#00aaaa" />
                    <rect x="26" y="42" width="8" height="22" fill="#3b3ba4" />
                    <g transform="translate(24, 22) rotate(20)">
                      <rect x="-4" y="0" width="8" height="24" fill="#f1b48b" />
                      <rect x="-4" y="0" width="8" height="12" fill="#00aaaa" />
                    </g>
                    <g transform="translate(20, 2)">
                      <rect x="0" y="0" width="16" height="16" fill="#f1b48b" />
                      <rect x="0" y="0" width="16" height="4" fill="#3a251c" />
                      <rect x="0" y="4" width="4" height="4" fill="#3a251c" />
                      <rect x="12" y="4" width="4" height="4" fill="#3a251c" />
                      <g className="steve-eyes">
                        <rect x="2" y="8" width="4" height="2" fill="#fff" />
                        <rect x="4" y="8" width="2" height="2" fill="#3b3ba4" />
                        <rect x="10" y="8" width="4" height="2" fill="#fff" />
                        <rect x="10" y="8" width="2" height="2" fill="#3b3ba4" />
                      </g>
                      <rect x="6" y="10" width="4" height="2" fill="#905030" />
                      <rect x="6" y="12" width="4" height="2" fill="#603020" />
                    </g>
                  </svg>
                </div>
              </span>
              {' '}on Your Policy
            </h1>
            <p className="hero-subtitle">
              Upload your Health Insurance policy for intelligent risk analysis, hidden charge detection, and benchmark scoring.
            </p>
            <div style={{ marginTop: '1.5rem' }}>
              <a href="#" className="supported-link" onClick={(e) => { e.preventDefault(); setShowProviders(true); }}>
                See which health insurance providers we are now supporting &rarr;
              </a>
            </div>
          </header>

          <main className="main-content fade-in">
            {!result ? (
              <section className="glass-panel upload-section">
                <DocumentDropzone onUploadSuccess={(data) => setResult(data)} />
              </section>
            ) : (
              <div className="fade-in">
                <PolicyScoreCard scoreData={result.policy_score} analysisData={result.analysis} />
                <div style={{ textAlign: 'center', marginTop: '2rem' }}>
                  <button className="btn-secondary" onClick={() => setResult(null)}>
                    Analyze Another Policy
                  </button>
                </div>
              </div>
            )}
          </main>
        </>
      )}

      <footer className="app-footer">
        <p>Created by Navonil, Puru, Shubham from BIT Mesra</p>
      </footer>
    </div>
  );
};

export default App;
