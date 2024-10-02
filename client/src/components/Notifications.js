import React, { useEffect, useState } from 'react';

// Notification functional component
const Notifications = () => {
    const [notifications, setNotifications] = useState([]); // State to store notifications
    const [error, setError] = useState(null); // State to track error

    // Fetch notifications on component mount
    useEffect(() => {
        const fetchNotifications = async () => {
            // Mock data for notifications
            const mockData = [
                { id: 1, message: 'Notification 1' },
                { id: 2, message: 'Notification 2' },
            ];
            setNotifications(mockData); // Set mock data directly
            // Removed error handling
        };

        fetchNotifications(); // Call the fetch function
    }, []);

    // Function to mark notification as read
    const markAsRead = async (notificationId) => {
        // Mock success response
        setNotifications(notifications.filter(notification => notification.id !== notificationId)); // Update state
        // Removed error handling
    };

    // Render notifications
    return (
        <div className="relative">
            <button className="flex items-center bg-blue-600 text-white p-2 rounded">
                Notifications
            </button>
            <div className="absolute right-0 w-60 mt-2 bg-white rounded shadow-lg z-10">
                {error && <div className="p-2 text-red-600">{error}</div>} {/* Display error message if any */}
                {notifications.length === 0 ? (
                    <div className="p-2">No notifications</div>
                ) : (
                    notifications.map(notification => (
                        <div key={notification.id} className="p-2 border-b" role="alert">
                            <p>{notification.message}</p>
                            <button
                                className="text-blue-500 hover:underline"
                                onClick={() => markAsRead(notification.id)}
                                aria-label={`Mark notification ${notification.id} as read`}
                            >
                                Mark as read
                            </button>
                        </div>
                    ))
                )}
            </div>
        </div>
    );
};

export default Notifications;