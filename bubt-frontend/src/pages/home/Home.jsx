import React from "react";
import { Container, Row, Col, Button } from "react-bootstrap";
import Lottie from "lottie-react";
import reading from "../../assets/json/reading.json";
import { Link } from "react-router-dom";
import './Home.css'

const Home = () => {
  return (
    <div class="home-container border">
      <Container className="mt-5 mb-5">
        <Row className="align-items-center justify-content-center gap-4 mt-lg-5">
          <Col lg={6} className="text-lg-start">
            <div class="text-container text-dark rounded">
              <div class="p-5 text-start">
                <h2 class="text-dark">Welcome BUBT University</h2>
                <p class="text-justify no-margin text-dark">
                  At Bangladesh University of Bussiness and Technology, we are
                  dedicated to excellence in education, research, and community
                  engagement. Join a diverse community of learners, innovators,
                  and leaders who are shaping the future across a broad range of
                  fields.
                </p>
              </div>
            </div>
          </Col>

          <Col lg={5} className="d-flex justify-content-center">
            <div className="w-100" style={{ maxWidth: "24rem" }}>
              <Lottie animationData={reading} loop={true} />
            </div>
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default Home;
