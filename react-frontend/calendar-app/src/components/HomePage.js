// src/components/HomePage.js
import React from "react";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const navigate = useNavigate();

  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>Welcome to the Calendar Application</h1>
      <div style={styles.buttonContainer}>
        <button style={styles.button} onClick={() => navigate("/admin-login")}>
          Admin Login
        </button>
        <button style={styles.button} onClick={() => navigate("/user-login")}>
          User Login
        </button>
        <button
          style={styles.button}
          onClick={() => navigate("/analytics-login")}
        >
          Report and Analytics Login
        </button>
      </div>
    </div>
  );
};

const styles = {
  container: {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    height: "100vh",
    backgroundColor: "#f4f4f9",
  },
  heading: {
    fontSize: "2rem",
    marginBottom: "2rem",
  },
  buttonContainer: {
    display: "flex",
    flexDirection: "column",
    gap: "1rem",
  },
  button: {
    padding: "1rem 2rem",
    fontSize: "1rem",
    backgroundColor: "#007bff",
    color: "#fff",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
    transition: "background-color 0.3s ease",
  },
  buttonHover: {
    backgroundColor: "#0056b3",
  },
};

export default HomePage;
