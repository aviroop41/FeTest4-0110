import React, { useEffect, useState } from 'react';

const CalendarIntegration = ({ employeeId }) => {
    const [events, setEvents] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [calendarProvider, setCalendarProvider] = useState('');
    const [credentials, setCredentials] = useState('');

    const fetchEvents = async (startDate, endDate) => {
        try {
            const response = await fetch(`http://localhost:8080/api/employee/${employeeId}/calendar/events?start_date=${startDate}&end_date=${endDate}`);
            if (!response.ok) throw new Error('Failed to fetch events');
            const data = await response.json();
            setEvents(data);
        } catch (error) {
            setError(error.message);
        } finally {
            setLoading(false);
        }
    };

    const linkCalendar = async () => {
        try {
            const response = await fetch(`http://localhost:8080/api/employee/${employeeId}/calendar/link`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ calendar_provider: calendarProvider, credentials })
            });
            if (!response.ok) throw new Error('Failed to link calendar');
            alert('Calendar linked successfully!');
        } catch (error) {
            setError(error.message);
        }
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
            {error && <div className="text-red-500 mb-4">{error}</div>}
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