import React from "react";
import { useQuery } from "@tanstack/react-query";
import axios from "axios";
import { Button, Card } from "react-bootstrap";
import './Faculties.css'


const fetchFaculties = async () => {
  const token = localStorage.getItem("token");
  const response = await axios.get(
    "http://127.0.0.1:8000/academic-utils/academic-faculties/",
    {
      headers: {
        Authorization: `JWT ${token}`,
      },
    }
  );
  return response.data;
};

const Faculties = () => {
  const { data, isLoading, isError, error } = useQuery({
    queryKey: ["faculties"],
    queryFn: fetchFaculties,
  });

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (isError) {
    return <div>Error: {error.message}</div>;
  }

  
  const colors = [
    "lightblue",
    "lightgreen",
    "lightblue",
    "lightcoral",
    "lightpink",
  ];

  return (
    <div>
      <h1
        className="text-center mt-3 text-decoration-underline"
        style={{ color: "#007bff" }}
      >
        Academic Faculties
      </h1>
      <div className="container mt-5">
        <div className="row d-flex justify-content-center align-items-center">
          {data.map((faculty, index) => (
            <div className="col-md-4 mb-4 cursor-pointer" key={faculty.id}>
              <Card
                style={{
                  width: "18rem",
                  height: "12rem",
                  backgroundColor: colors[index % colors.length],
                }}
                className="faculty-card"
              >
                <Card.Body className="d-flex flex-column justify-content-center align-items-center">
                  <Card.Title>{faculty.name}</Card.Title>
                  <Button variant="primary">See Details</Button>
                </Card.Body>
              </Card>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Faculties;
