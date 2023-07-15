import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import './MyForm.scss';
import Select from 'react-select';
import loading from '../assets/Loading.json';
import lottie from 'lottie-web';

function MyForm() {
  const [inputValue, setInputValue] = useState('');
  const [showLanguageButtons, setShowLanguageButtons] = useState(false);
  const [language, setLanguage] = useState({});
  const [selectedOption, setSelectedOption] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [summary, setSummary] = useState('');
  const animationContainerRef = useRef(null);
  const animationRef = useRef(null);

  useEffect(() => {
    const container = animationContainerRef.current;
    const startLoader = () => {
      animationRef.current = lottie.loadAnimation({
        container,
        animationData: loading,
        renderer: 'svg',
        loop: true,
        autoplay: true,
      });
    };

    const stopLoader = () => {
      if (animationRef.current) {
        animationRef.current.destroy();
        animationRef.current = null;
      }
    };

    if (isLoading) {
      startLoader();
    } else {
      stopLoader();
    }

    return () => {
      stopLoader();
    };
  }, [isLoading]);

  const handleSubmit = async () => {
    let requestedData = {
      youtube_link: inputValue,
      language: selectedOption?.value,
    };
    setIsLoading(true);
    if (selectedOption?.value) {
      await axios
        .post('http://127.0.0.1:8000/api/getSummary/', {
          youtube_link: requestedData.youtube_link,
          language: requestedData.language,
        })
        .then((response) => {
          setSummary(response.data.summary);
        })
        .catch((error) => {
          console.error(error);
          setSummary('BAD REQUEST');
        })
        .finally(() => {
          setIsLoading(false);
        });
    } else {
      await axios
        .post('http://127.0.0.1:8000/api/tfidfSummary/', {
          youtube_link: requestedData.youtube_link,
        })
        .then((response) => {
          console.log(response.data.summary);
          setSummary(response.data.summary);
        })
        .catch((error) => {
          console.error(error);
          setSummary('BAD REQUEST');
        })
        .finally(() => {
          setIsLoading(false);
        });
    }
  };

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleAbstractiveSummarization = async () => {
    setShowLanguageButtons(true);
    await axios
      .post('http://127.0.0.1:8000/api/getLanguages/', {
        youtube_link: inputValue,
      })
      .then((response) => {
        setLanguage(response.data.body);
        console.log(response.data.body);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <>
      <div className='form'>
        <input
          type='text'
          value={inputValue}
          onChange={handleInputChange}
          placeholder='Youtube Video Link...'
          className='input-field'
        />
        <label>
          <input type='radio' name='option' value='ExtractiveSummarization' />
          <span className='labs'>Extractive Summarization</span>
        </label>
        <label>
          <input
            type='radio'
            name='option'
            value='AbstractiveSummarization'
            onClick={handleAbstractiveSummarization}
          />
          <span className='labs'>Abstractive Summarization</span>
        </label>
        {showLanguageButtons && (
          <Select
            defaultValue={selectedOption}
            onChange={setSelectedOption}
            options={Object.entries(language).map(([value, label]) => ({
              value,
              label,
            }))}
          />
        )}
        {isLoading && <div id='loading-logo' ref={animationContainerRef} />}
        <button onClick={handleSubmit}>Submit</button>
        {summary !== '' && (
          <div className='summary'>
            <span className='data'>{summary}</span>
          </div>
        )}
        {console.log(summary)}
      </div>
    </>
  );
}
export default MyForm;
