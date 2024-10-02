import React, { useEffect, useState } from 'react';
import ProfileManagement from '../components/ProfileManagement';
import CalendarIntegration from '../components/CalendarIntegration'; // Importing the CalendarIntegration component

const ProfilePage = () => {
    const [profileData, setProfileData] = useState(null);
    const [error, setError] = useState(null);
    const [calendarEvents, setCalendarEvents] = useState([]); // State for storing calendar events
    const [loadingEvents, setLoadingEvents] = useState(true); // State for loading calendar events

    useEffect(() => {
        const fetchProfileData = async () => {
            try {
                const response = await fetch('http://localhost:8080/api/employee/1/profile');
                if (!response.ok) {
                    throw new Error('Failed to fetch profile data');
                }
                const data = await response.json();
                setProfileData(data);
            } catch (err) {
                // Mock data in case of fetch failure
                setProfileData({
                    name: 'John Doe',
                    email: 'john.doe@example.com',
                    contact_number: '123-456-7890',
                    address: '123 Main St, Anytown, USA',
                });
                setError(err.message);
            }
        };

        const fetchCalendarEvents = async () => {
            setLoadingEvents(true);
            try {
                const response = await fetch('http://localhost:8080/api/employee/1/calendar/events?start_date=2023-01-01&end_date=2023-12-31');
                if (!response.ok) {
                    throw new Error('Failed to fetch calendar events');
                }
                const eventsData = await response.json();
                setCalendarEvents(eventsData);
            } catch (err) {
                // Mock calendar events data in case of fetch failure
                setCalendarEvents([
                    { id: 1, title: 'Team Meeting', date: '2023-10-15', time: '10:00 AM' },
                    { id: 2, title: 'Project Deadline', date: '2023-10-20', time: '5:00 PM' },
                    { id: 3, title: 'Client Call', date: '2023-10-22', time: '3:00 PM' },
                ]);
                setError(err.message);
            } finally {
                setLoadingEvents(false);
            }
        };

        fetchProfileData();
        fetchCalendarEvents();
    }, []);

    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold mb-4">Profile Management</h1>
            {profileData ? (
                <ProfileManagement profile={profileData} />
            ) : (
                <p>Loading profile...</p>
            )}
            <h2 className="text-xl font-semibold mt-6">Calendar Integration</h2>
            {loadingEvents ? (
                <p>Loading calendar events...</p>
            ) : (
                <CalendarIntegration events={calendarEvents} /> // Integrating CalendarIntegration component
            )}
        </div>
    );
};

export default ProfilePage;