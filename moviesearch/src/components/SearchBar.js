import React, { useState } from 'react';
import '../App.css';

function SearchBar({ onSearch }) {
  const [query, setQuery] = useState('');
  const [site, setSite] = useState('All Sites');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(query, site);
  };

  return (
    <div id="rectangle">
      <form onSubmit={handleSubmit}>
        <input
          id="matrix"
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Matrix"
        />
        <select
          id="all-sites"
          value={site}
          onChange={(e) => setSite(e.target.value)}
        >
          <option value="All Sites">All Sites</option>
          {/* Add more site options here */}
        </select>
        <button id="search" type="submit">
          Search
        </button>
      </form>
    </div>
  );
}

export default SearchBar;
