'use strict';

const outputFile = '../data/tree-data.csv';
const fs = require('fs');

const json = JSON.parse(fs.readFileSync('../data/ncov.json'));

const header = ['name', 'mutations', 'calde', 'division', 'nuc'];

let rows = [];

json.tree.children.forEach(processTreeNode);
console.log(rows);
rows = rows.filter(row => !!row).map(row => {
  return [row.name, row.mutations, row.clade, row.division, row.nuc].join(', ');
}).join('\n');
fs.writeFileSync(outputFile, header.join(', ')+'\n'+rows)

function processTreeNode(node){
  let entry = {};
  entry['name'] = node.name;
  entry['division'] = node.node_attrs.division.value;
  if (node.branch_attrs && node.branch_attrs.labels) {
    entry['mutations'] = node.branch_attrs.labels.aa;
    entry['clade'] = node.branch_attrs.labels.clade;
  }
  if (node.branch_attrs && node.branch_attrs.mutations && node.branch_attrs.mutations.nuc) {
    entry['nuc'] = node.branch_attrs.mutations.nuc.join('; ');
  }

  rows.push(entry);

  if (node.children && node.children.length > 0) {
    node.children.map(processTreeNode)
      .forEach(arr => {
        rows = rows.concat(arr);
      });
  }
}