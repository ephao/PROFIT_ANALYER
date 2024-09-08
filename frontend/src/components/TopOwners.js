import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TopOwners = () => {
  const [owners, setOwners] = useState([]);
  const [numOwners, setNumOwners] = useState(10);

  useEffect(() => {
    fetchOwners();
  }, [numOwners]);

  const fetchOwners = async () => {
    try {
      const response = await axios.get(`http://localhost:5000/api/top_profitable_owners?n=${numOwners}`);
      setOwners(response.data);
    } catch (error) {
      console.error('Error fetching top owners:', error);
    }
  };

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