import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TopOwners = () => {
  // React component for displaying top profitable owners
  // State:
  //   owners: Array of top owner objects
  //   numOwners: Number of top owners to display

  const [owners, setOwners] = useState([]);
  const [numOwners, setNumOwners] = useState(10);

  useEffect(() => {
    fetchOwners();
  }, [numOwners]);  // Fetch owners when numOwners changes

  const fetchOwners = async () => {
    // Fetches top owners data from the API
    try {
      const response = await axios.get(`http://localhost:5000/api/top_profitable_owners?n=${numOwners}`);
      setOwners(response.data);
    } catch (error) {
      console.error('Error fetching top owners:', error);
    }
  };

  // Renders a list of top owners with an input to adjust the number of displayed owners
  return (
    <div>
      <h2>Top {numOwners} Profitable Owners</h2>
      <input
        type="number"
        value={numOwners}
        onChange={(e) => setNumOwners(e.target.value)}
        min="1"
      />
      <ul>
        {owners.map((owner, index) => (
          <li key={index}>
            Address: {owner.address}, Total Profit: ${owner.total_profit.toFixed(2)}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TopOwners;