import React, { useEffect, useState } from 'react';

// Notification functional component
const Notifications = () => {
    const [notifications, setNotifications] = useState([]); // State to store notifications
    const [error, setError] = useState(null); // State to track error

    // Fetch notifications on component mount
    useEffect(() => {
        const fetchNotifications = async () => {
            try {
                const response = await fetch('/api/employee/1/notifications'); // Replace '1' with dynamic employee_id
                if (!response.ok) throw new Error('Failed to fetch notifications');
                const data = await response.json();
                setNotifications(data);
            } catch (err) {
                setError(err.message); // Update error state if fetch fails
            }
        };

        fetchNotifications(); // Call the fetch function
    }, []);

    // Function to mark notification as read
    const markAsRead = async (notificationId) => {
        try {
            const response = await fetch(`/api/employee/1/notifications/${notificationId}/read`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            if (!response.ok) throw new Error('Failed to mark notification as read');
            setNotifications(notifications.filter(notification => notification.id !== notificationId)); // Update state
        } catch (err) {
            setError(err.message);
        }
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