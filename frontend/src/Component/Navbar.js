import React from 'react';
import styled from 'styled-components';
import Logo from '../Assets/logo.png'; 
import { FaInstagram, FaFacebookF, FaTwitter } from 'react-icons/fa'; 

const Nav = styled.nav`
  background-color: white;  /* White background */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Add a shadow for a professional look */
  padding: 0.5rem 1rem; /* Add padding for a cleaner layout */
  height: 80px;
`;

const NavWrapper = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
`;

const BrandLogo = styled.img`
  width: 200px;
`;

const NavList = styled.ul`
  display: flex;
  list-style-type: none;
  margin: 0;
  padding: 0;
`;

const NavItem = styled.li`
  margin-left: 20px;
`;

const NavLink = styled.a`
  color: black; /* Black color for the links */
  font-size: 1.2rem;
  font-weight: 600;
  text-transform: uppercase;
  text-decoration: none;
  transition: color 0.3s ease;
//   padding-top: 6px;

  &:hover {
    color: #ff9800; /* A vibrant color on hover */
  }
`;

const SocialLinks = styled.div`
  display: flex;
  align-items: center;
  padding-top: 3px;
  gap: 10px;
`;

const SocialIcon = styled.a`
  color: black;
  font-size: 1.5rem;
  margin-left: 15px;
  transition: color 0.3s ease;

  &:hover {
    color: #ff9800; /* Hover color */
  }
`;

const Navbar = () => {
  return (
    <Nav>
      <NavWrapper>
        <BrandLogo src={Logo} alt="Logo" />
        
        <div style={{
            display: 'flex',
            flexDirection: 'row',

        }}>

        <NavList>
          <NavItem>
            <NavLink href="https://clinicaltrials.gov/" target="_blank" rel="noopener noreferrer">
              Data Source
            </NavLink>
          </NavItem>
        </NavList>

        <SocialLinks>
          <SocialIcon href="https://www.instagram.com/novartis/?hl=en" target="_blank" rel="noopener noreferrer">
            <FaInstagram />
          </SocialIcon>
          <SocialIcon href="https://www.facebook.com/novartis/" target="_blank" rel="noopener noreferrer">
            <FaFacebookF />
          </SocialIcon>
          <SocialIcon href="https://twitter.com/novartis?" target="_blank" rel="noopener noreferrer">
            <FaTwitter />
          </SocialIcon>
        </SocialLinks>
        </div>
      </NavWrapper>
    </Nav>
  );
};

export default Navbar;
