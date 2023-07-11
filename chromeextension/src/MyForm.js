import React, { useState } from 'react';
import axios from 'axios';

function MyForm() {
  const [inputValue, setInputValue] = useState('');
  var data = '';
  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('sent');
    axios
      .post('http://127.0.0.1:8000/api/summarize/', {
        youtube_link: inputValue,
      })
      .then((response) => {
        console.log(response.data);
        data = response.data;
      })
      .catch((error) => {
        console.error(error);
      });
  };

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <label>
          <input type='text' value={inputValue} onChange={handleInputChange} />
        </label>
        <br />
        <button type='submit'>Submit</button>
      </form>
      <div id='apiData'>{data}</div>
    </>
  );
}

export default MyForm;
