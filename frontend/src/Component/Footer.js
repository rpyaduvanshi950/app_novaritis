import React from 'react';
import styled from 'styled-components';

const FooterContainer = styled.footer`
  background-color: #333; /* Dark background for contrast */
  color: #fff; /* White text */
  padding: .8rem 0;
  text-align: center;
  font-size: 0.9rem;
  position: absolute;
    // bottom: 0;
    width: 100%;
    // height: 100px;
`;

const FooterContent = styled.div`
  max-width: 1200px;
  margin: 0 auto;
`;

const FooterLinks = styled.ul`
  list-style: none;
  padding: 0;
  margin: .5rem 0;
  display: flex;
  justify-content: center;
//   gap: 2rem;
`;

const FooterLinkItem = styled.li``;

const FooterLink = styled.a`
  color: #fff;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease;

  &:hover {
    color: #ff9800; /* Add hover effect for better interactivity */
  }
`;

const FooterText = styled.p`
  margin-top: .5rem;
  font-size: 0.8rem;
`;

const Footer = () => {
  return (
    <FooterContainer>
      <FooterContent>
        <FooterLinks>
          <FooterLinkItem>
            <FooterLink  target="_blank" rel="noopener noreferrer">
              Developed by Satyam Team
            </FooterLink>
          </FooterLinkItem>
        </FooterLinks>
        <FooterText>
          &copy; {new Date().getFullYear()} NOVARTIS. All rights reserved.
        </FooterText>
      </FooterContent>
    </FooterContainer>
  );
};

export default Footer;
