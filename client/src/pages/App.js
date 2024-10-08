import React, { useEffect, useState } from 'react'; // Importing React and necessary hooks
import Header from '../components/Header'; // Importing Header component
import Footer from '../components/Footer'; // Importing Footer component
import Sidebar from '../components/Sidebar'; // Importing Sidebar component

const App = () => {
    const [data, setData] = useState([]); // State to hold fetched data
    const [error, setError] = useState(null); // State for error handling

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://localhost:8080/api/data'); // Fetching data from API
                if (!response.ok) {
                    throw new Error('Network response was not ok'); // Error handling for network issues
                }
                const result = await response.json(); // Parsing JSON response
                setData(result); // Updating state with fetched data
            } catch (error) {
                // Mock data in case of failure
                setData([
                    { id: 1, title: 'Sample Item 1', description: 'Description for item 1.' },
                    { id: 2, title: 'Sample Item 2', description: 'Description for item 2.' },
                    { id: 3, title: 'Sample Item 3', description: 'Description for item 3.' },
                ]);
                setError(error.message); // Setting error message in state
            }
        };

        fetchData(); // Calling the fetchData function
    }, []); // Empty dependency array means this useEffect runs once on mount

    return (
        <div className="flex flex-col min-h-screen"> {/* Main container for flex layout */}
            <Header /> {/* Render Header component */}
            <div className="flex flex-row min-h-full"> {/* Flex layout for sidebar and main content */}
                <Sidebar /> {/* Render Sidebar component */}
                <main className="flex-grow px-4 py-8"> {/* Main content area with padding */}
                    {error ? ( // Conditional rendering based on error state
                        <div className="text-red-600">{error}</div> // Display error message
                    ) : (
                        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3"> {/* Responsive grid layout */}
                            {data.map(item => ( // Mapping over fetched data
                                <div key={item.id} className="p-4 border border-gray-200 rounded shadow"> {/* Card for each item */}
                                    <h2 className="font-bold">{item.title}</h2> {/* Item title */}
                                    <p>{item.description}</p> {/* Item description */}
                                </div>
                            ))}
                        </div>
                    )}
                </main>
            </div>
            <Footer /> {/* Render Footer component */}
        </div>
    );
};

export default App; // Exporting App component.