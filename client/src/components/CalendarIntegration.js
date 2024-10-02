import React, { useEffect, useState } from 'react';

const CalendarIntegration = ({ employeeId }) => {
    const [events, setEvents] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [calendarProvider, setCalendarProvider] = useState('');
    const [credentials, setCredentials] = useState('');

    const mockEvents = [
        { id: 1, title: 'Meeting with Team', start: '2023-10-01T10:00:00Z', end: '2023-10-01T11:00:00Z' },
        { id: 2, title: 'Project Deadline', start: '2023-10-05T12:00:00Z', end: '2023-10-05T13:00:00Z' },
        { id: 3, title: 'Client Call', start: '2023-10-10T14:00:00Z', end: '2023-10-10T15:00:00Z' },
        { id: 4, title: 'Team Lunch', start: '2023-10-15T12:00:00Z', end: '2023-10-15T13:00:00Z' },
    ];

    const fetchEvents = async (startDate, endDate) => {
        // Mocking data instead of fetching
        setEvents(mockEvents);
        setLoading(false);
    };

    const linkCalendar = async () => {
        // Mocking successful linking
        alert('Calendar linked successfully!');
    };

    useEffect(() => {
        const startDate = new Date();
        const endDate = new Date();
        endDate.setMonth(endDate.getMonth() + 1);
        fetchEvents(startDate.toISOString(), endDate.toISOString());
    }, []);

    return (
        <div className="p-6 bg-white rounded-lg shadow-md">
            <h2 className="text-xl font-semibold mb-4">Calendar Integration</h2>
            <div className="mb-4">
                <label className="block mb-2">Calendar Provider</label>
                <input
                    type="text"
                    value={calendarProvider}
                    onChange={(e) => setCalendarProvider(e.target.value)}
                    className="input input-bordered w-full"
                    aria-label="Calendar Provider"
                />
            </div>
            <div className="mb-4">
                <label className="block mb-2">Credentials</label>
                <input
                    type="text"
                    value={credentials}
                    onChange={(e) => setCredentials(e.target.value)}
                    className="input input-bordered w-full"
                    aria-label="Credentials"
                />
            </div>
            <button onClick={linkCalendar} className="btn btn-primary mb-4">Link Calendar</button>
            {loading ? (
                <p>Loading events...</p>
            ) : (
                <ul className="list-disc pl-5">
                    {events.map((event) => (
                        <li key={event.id} className="mb-2">
                            {event.title} - {new Date(event.start).toLocaleString()} to {new Date(event.end).toLocaleString()}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default CalendarIntegration;