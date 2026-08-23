import React from 'react';

interface PolicyScoreCardProps {
  scoreData: any;
  analysisData: any;
}

export const PolicyScoreCard: React.FC<PolicyScoreCardProps> = ({ scoreData, analysisData }) => {
  return (
    <div className="glass-panel" style={{ padding: '2rem', marginTop: '2rem' }}>
      <h2 className="gradient-text" style={{ marginTop: 0 }}>Analysis Complete</h2>
      
      <div style={{ display: 'flex', gap: '2rem', flexWrap: 'wrap' }}>
        <div style={{ flex: 1, minWidth: '300px', background: 'rgba(0,0,0,0.2)', padding: '1.5rem', borderRadius: 'var(--radius-md)' }}>
          <h3 style={{ margin: '0 0 1rem 0', color: 'var(--text-secondary)' }}>Deterministic Policy Score</h3>
          <h1 style={{ fontSize: '3rem', margin: '0 0 0.5rem 0', color: scoreData.overall_score > 70 ? 'var(--risk-low)' : 'var(--risk-high)' }}>
            {scoreData.overall_score} / 100
          </h1>
          <p>Verdict: <strong>{scoreData.verdict}</strong></p>
          <div style={{ display: 'flex', gap: '1rem', fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
            <span>Trust: {scoreData.trust_score}</span>
            <span>Transparency: {scoreData.transparency_score}</span>
          </div>
        </div>
        
        <div style={{ flex: 2, minWidth: '300px', background: 'rgba(0,0,0,0.2)', padding: '1.5rem', borderRadius: 'var(--radius-md)' }}>
          <h3 style={{ margin: '0 0 1rem 0', color: 'var(--text-secondary)' }}>AI RAG Clause Analysis</h3>
          <h4 style={{ margin: '0 0 0.5rem 0' }}>{analysisData.title}</h4>
          <p style={{ margin: '0 0 1rem 0' }}>{analysisData.summary}</p>
          
          <div style={{ padding: '1rem', background: 'rgba(245, 158, 11, 0.1)', borderLeft: '4px solid var(--risk-medium)' }}>
            <strong>Why Flagged:</strong> {analysisData.why_flagged}
          </div>
          
          <div style={{ padding: '1rem', background: 'rgba(16, 185, 129, 0.1)', borderLeft: '4px solid var(--risk-low)', marginTop: '1rem' }}>
            <strong>Recommendation:</strong> {analysisData.recommendation}
          </div>
        </div>
      </div>
    </div>
  );
};
