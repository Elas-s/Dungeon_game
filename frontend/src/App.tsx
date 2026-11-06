import ScoreRow from './ScoreRow'

function App() {
  return (
      <main>
        <h1>🏆 Hall of Fame</h1>
        <ScoreRow rank={1} name="Elass" gold={180}/>
        <ScoreRow rank={2} name="Budda" gold={179}/>
        <ScoreRow rank={3} name="Petur" gold={1}/>
        <ScoreRow rank={4} name="air" gold={5}/>
      </main>
  )
}

export default App