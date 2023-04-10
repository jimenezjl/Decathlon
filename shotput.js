let max_shotput = 0;

function attempt() {
  let total_shotput = [];
  let results = [];
  for (let i = 0; i < 3; i++) {
    let total_score = 0;
    let num_of_dice = 0;
    console.log(`INTENTO ${i + 1}/3`);
    prompt("Pulsa enter para lanzar");
    while (num_of_dice < 8) {
      num_of_dice++;
      let dice_roll = Math.floor(Math.random() * 6) + 1;
      total_score += dice_roll;
      console.log(`Dado ${num_of_dice}: ${dice_roll}, Suma: ${total_score}`);
      if (dice_roll === 1) {
        console.log(`¡Has sacado un 1 en el dado ${num_of_dice}! Tu lanzamiento se considera nulo.`);
        total_score = 0;
        break;
      }
      if (num_of_dice === 8) {
        total_shotput.push(total_score);
        results.push([i + 1, total_score]);
        console.log(`Lanzamiento ${i + 1} terminado, puntuación total: ${total_score}`);
        if (total_score > max_shotput) {
          max_shotput = total_score;
        }
        break;
      }
      let response = prompt("Si quieres continuar lanzando, pulsa s, si quieres parar el lanzamiento pulsa n, (s/n): ");
      if (response.toLowerCase() !== 's') {
        total_shotput.push(total_score);
        results.push([i + 1, total_score]);
        console.log(`Lanzamiento ${i + 1} terminado, puntuación total: ${total_score}`);
        if (total_score > max_shotput) {
          max_shotput = total_score;
        }
        break;
      }
    }
    if (total_score === 0) {
      results.push([i + 1, "Lanzamiento nulo"]);
    }
  }
  console.log("Resultados:");
  results.forEach((row, i) => {
    if (typeof row[1] === 'number') {
      if (row[1] === max_shotput) {
        console.log(`Lanzamiento ${row[0]}: \x1b[1m${row[1]}\x1b[0m (máximo)`);
      } else {
        console.log(`Lanzamiento ${row[0]}: ${row[1]}`);
      }
    } else {
      console.log(`Lanzamiento ${row[0]}: ${row[1]}`);
    }
  });
