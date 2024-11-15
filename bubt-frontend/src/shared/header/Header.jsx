import React, { useState } from 'react'
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
import './Header.css';

const Header = () => {

  // assume user already loged in.............
  const [isLogedUser, setIsLogedUser] = useState(true)


  return (
    <div class="header-container">
      <Navbar expand="lg" className="bg-body-tertiary">
        <Container>
          <Navbar.Brand href="/">BUBT</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="m-auto">
              <Nav.Link href="/">Home</Nav.Link>
              <Nav.Link href="#course">Courses</Nav.Link>
              <Nav.Link href="#blog">Blogs</Nav.Link>
              <Nav.Link href="/faculties">Faculties</Nav.Link>
              <Nav.Link href="#about">About</Nav.Link>
              <Nav.Link href="#apply">Apply Now</Nav.Link>
              {/* <NavDropdown title="Faculties" id="basic-nav-dropdown">
                <NavDropdown.Item href="#action/3.1"></NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">
                  Another action
                </NavDropdown.Item>
                <NavDropdown.Item href="#action/3.3">
                  Something
                </NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#action/3.4">
                  Separated link
                </NavDropdown.Item>
              </NavDropdown> */}
            </Nav>
            <div class="d-flex justify-content-center align-items-center gap-3">
              {isLogedUser ? (
                <Nav.Link href="#login">Login</Nav.Link>
              ) : (
                <Nav.Link href="#logout">Logout</Nav.Link>
              )}
            </div>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </div>
  );
}

export default Header
