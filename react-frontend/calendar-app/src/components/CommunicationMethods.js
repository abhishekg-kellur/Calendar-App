// File: src/components/CommunicationMethods.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const CommunicationMethods = () => {
  const [methods, setMethods] = useState([]);

  useEffect(() => {
    axios.get('/api/communication-methods')
      .then((response) => setMethods(response.data))
      .catch((error) => console.error('Error fetching communication methods:', error));
  }, []);

  return (
    <div className="communication-methods">
      <h2>Communication Methods</h2>
      <button>Add Communication Method</button>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Sequence</th>
            <th>Mandatory</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {methods.map((method) => (
            <tr key={method.id}>
              <td>{method.name}</td>
              <td>{method.description}</td>
              <td>{method.sequence}</td>
              <td>{method.mandatory ? 'Yes' : 'No'}</td>
              <td>
                <button>Edit</button>
                <button>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CommunicationMethods;
