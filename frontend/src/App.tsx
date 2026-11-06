import { useEffect, useState } from 'react'
import ScoreRow from './ScoreRow'

type Score = { name: string; gold: number }
type Stats = {
  games: number
  average_gold: number
  most_active: { name: string; games: number } | null
}

const API = 'http://localhost:8000'

function App() {
  const [scores, setScores] = useState<Score[]>([])
  const [stats, setStats] = useState<Stats | null>(null)
  const [error, setError] = useState(false)

  useEffect(() => {
    fetch(`${API}/scores`)
      .then((response) => response.json())
      .then((data) => setScores(data))
      .catch(() => setError(true))

    fetch(`${API}/stats`)
      .then((response) => response.json())
      .then((data) => setStats(data))
      .catch(() => setError(true))
  }, [])

  const podium = scores.slice(0, 3)
  const rest = scores.slice(3)

  return (
    <main className="page">
      <header className="header">
        <div className="candles">🕯️ 🏰 🕯️</div>
        <h1>Hall of Fame</h1>
        {error ? (
          <p className="live offline">The dungeon API is asleep. Start it with uv run uvicorn api:app</p>
        ) : (
          <p className="live"><span className="dot"></span> live from the dungeon API</p>
        )}
      </header>

      {scores.length === 0 && !error && (
        <p className="empty">No heroes yet... go escape the dungeon! ⚔️</p>
      )}

      <section className="podium">
        {/* order on screen: 2nd, 1st, 3rd */}
        {[1, 0, 2].map((i) =>
          podium[i] ? (
            <div key={i} className={`spot place-${i + 1}`}>
              {i === 0 && <div className="crown">👑</div>}
              <div className="who">{podium[i].name}</div>
              <div className="gold">💰 {podium[i].gold} gold</div>
              <div className="block">{i + 1}</div>
            </div>
          ) : null
        )}
      </section>

      <section className="rest">
        {rest.map((score, i) => (
          <ScoreRow key={i} rank={i + 4} name={score.name} gold={score.gold} />
        ))}
      </section>

      {stats && (
        <section className="stats">
          <div className="stat">
            <small>Games played</small>
            <strong>{stats.games}</strong>
          </div>
          <div className="stat">
            <small>Average gold</small>
            <strong>{stats.average_gold}</strong>
          </div>
          <div className="stat">
            <small>Most active</small>
            <strong>{stats.most_active?.name ?? '-'}</strong>
            {stats.most_active && <span> · {stats.most_active.games} games</span>}
          </div>
        </section>
      )}
    </main>
  )
}

export default App
