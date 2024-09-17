// Import React and axios
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const App = () => {
  const [title, setTitle] = useState('');
  const [sitename, setSitename] = useState('https://real-fmovies.show/');
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [sitenameOptions, setSitenameOptions] = useState(['https://real-fmovies.show/']);


  const fetchData = async () => {
    try {

      const params = { title };
      if (sitename) {
        params.sitename = sitename;
      }


      const response = await axios.get('http://127.0.0.1:8000/movies/getMovie/', { params });
      setData(response.data);

      const uniqueSitenameOptions = Array.from(new Set(response.data.map(item => item.sitename)));
      setSitenameOptions(uniqueSitenameOptions);
    } catch (err) {
      // setError(err.message);
      setError("Search Not found");
    }
  };

  return (
    <div className="centered-div">
      <h1 class="tHeader">Film & TV Extractor</h1>
      <table class="tablefilter">
        <tr>
          <td>
            <input
              className="filmtitle"
              type="text"
              placeholder="Search TV or Film"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            />
          </td>

          <td>
            <select value={sitename} onChange={(e) => setSitename(e.target.value)}
            >
              {sitenameOptions.map((option, index) => (
                <option key={index} value={option}>{option}</option>
              ))}
            </select>
          </td>

          <td>
          <button onClick={fetchData}>Search</button>
          </td>

        </tr>
      </table>
      <br/>
      <br/>

      {data && data.length > 0 && (
        <div>{data.length} Result{data.length > 1 ? 's' : ''}</div>
      )}
      <br/>

      {data && (
        <table>
          <thead>
            <tr>
              <th></th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {data.map((item, index) => (
              <tr key={index}>
                <td>
                  <img
                    src={item.image}
                    alt={item.title}
                    style={{ width: '100px', height: '100px' }}
                  />
                </td>
                <td>
                  <b>Title: </b> {item.title}
                  <br/>
                  <b>Page: </b><a href={item.pagelink} target="_blank" rel="noopener noreferrer">
                    {item.pagelink}
                  </a>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {error && <p>Error: {error}</p>}
    </div>
  );
};

export default App;
