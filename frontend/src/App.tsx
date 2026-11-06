import { useEffect, useState } from 'react'
import ScoreRow from './ScoreRow'

type Score = { name: string; gold: number }

function App() {
  const [scores, setScores] = useState<Score[]>([])

  useEffect(() => {
    fetch('http://localhost:8000/scores')
      .then((response) => response.json())
      .then((data) => setScores(data))
  }, [])

  return (
    <main>
      <h1>🏆 Hall of Fame</h1>
      {scores.map((score, i) => (
        <ScoreRow key={i} rank={i + 1} name={score.name} gold={score.gold} />
      ))}
    </main>
  )
}

export default App