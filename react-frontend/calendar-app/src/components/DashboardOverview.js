// File: src/components/DashboardOverview.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const DashboardOverview = () => {
  const [stats, setStats] = useState({ companies: 0, methods: 0 });

  useEffect(() => {
    axios.get('/api/dashboard-stats')
      .then((response) => setStats(response.data))
      .catch((error) => console.error('Error fetching stats:', error));
  }, []);

  return (
    <div className="dashboard-overview">
      <h2>Dashboard Overview</h2>
      <p>Total Companies: {stats.companies}</p>
      <p>Total Communication Methods: {stats.methods}</p>
    </div>
  );
};

export default DashboardOverview;