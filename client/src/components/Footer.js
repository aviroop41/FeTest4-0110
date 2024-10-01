import React from 'react';

// Footer Component
const Footer = () => {
  // Mock data in case of API failure
  const links = [
    { name: 'Privacy Policy', url: '/privacy' },
    { name: 'Terms of Service', url: '/terms' },
    { name: 'Contact Us', url: '/contact' },
  ];

  return (
    <footer className="bg-gray-100 text-center py-4 mt-10">
      <div className="container mx-auto">
        <nav aria-label="Footer Navigation">
          <ul className="flex justify-center space-x-4">
            {links.map((link) => (
              <li key={link.name}>
                <a 
                  href={link.url} 
                  className="text-gray-600 transition-colors duration-300 hover:text-gray-900"
                  // Semantic HTML for accessibility
                  aria-label={link.name}
                >
                  {link.name}
                </a>
              </li>
            ))}
          </ul>
        </nav>
      </div>
    </footer>
  );
};

export default Footer;