const data = new Date(sheet.getRange("B2").getValue() as string);
const valor = Number(sheet.getRange("B3").getValue());
const descricao = String(sheet.getRange("B4").getValue()).trim();
const categoria = String(sheet.getRange("B5").getValue()).trim();
const tipo = String(sheet.getRange("B6").getValue()).trim();

const parcelado = String(sheet.getRange("B7").getValue()).trim().toLowerCase();

if (!valor || valor <= 0) {
  throw new Error("Informe um valor válido em B3.");
}

if (!descricao) {
  throw new Error("Informe uma descrição em B4.");
}

if (parcelado !== "sim") {
  table.addRow(-1, [data, valor, descricao, categoria, tipo]);
  return;
}

const parcelas = Number(sheet.getRange("B8").getValue());

if (!parcelas || parcelas <= 0) {
  throw new Error("Informe uma quantidade de parcelas válida em B8.");
}