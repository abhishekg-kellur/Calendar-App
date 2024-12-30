// File: src/components/CompanyManagement.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const CompanyManagement = () => {
  const [companies, setCompanies] = useState([]);

  useEffect(() => {
    axios.get('/api/companies')
      .then((response) => setCompanies(response.data))
      .catch((error) => console.error('Error fetching companies:', error));
  }, []);

  return (
    <div className="company-management">
      <h2>Company Management</h2>
      <button>Add Company</button>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Location</th>
            <th>LinkedIn Profile</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {companies.map((company) => (
            <tr key={company.id}>
              <td>{company.name}</td>
              <td>{company.location}</td>
              <td><a href={company.linkedinProfile}>View</a></td>
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

export default CompanyManagement;
