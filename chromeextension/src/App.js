import React, { useEffect, useRef } from 'react';
import './App.scss';
import lottie from 'lottie-web';
import youtubeLogo from './assets/youtube.json';
import MyForm from './components/MyForm';

function App() {
  const animationContainerRef = useRef(null);
  useEffect(() => {
    const container = animationContainerRef.current;
    const animation = lottie.loadAnimation({
      container,
      animationData: youtubeLogo,
      renderer: 'svg',
      loop: true,
      autoplay: true,
    });
    return () => {
      animation.destroy();
    };
  }, []);

  return (
    <div className='app-root'>
      <span>YT Transcript Summarizer</span>
      <div id='youtube-logo' ref={animationContainerRef} />
      <MyForm />
    </div>
  );
}

export default App;
