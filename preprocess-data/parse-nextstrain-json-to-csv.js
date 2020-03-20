'use strict';

const outputFile = '../data/processed/tree-data.csv';
const fs = require('fs');

const json = JSON.parse(fs.readFileSync('../data/ncov.json'));

// table header
const header = [
  'name',
  'mutations',
  'clade',
  'division',
  'country',
  'nuc',
  'sampling_date', // num_date
  'originating_lab', 
  'submitting_lab',
  'GISAID_EPI_ISL',
  'GenBank_accession'
];

let rows = [];

json.tree.children.forEach(processTreeNode);

rows = rows.filter(row => !!row).map(row => {
  return [
    row.name,
    row.mutations, 
    row.clade,
    row.division,
    row.country,
    row.nuc,
    row.sampling_date,
    row.originating_lab,
    row.submitting_lab,
    row.gisaid,
    row.genbank
  ].join(', ');
}).join('\n');
fs.writeFileSync(outputFile, header.join(', ')+'\n'+rows)

function processTreeNode(node){
  let entry = {};
  // mutation name
  entry['name'] = node.name;

  // get division
  entry['division'] = node.node_attrs.division.value;
  // country if exists
  if (node.node_attrs && node.node_attrs.country) {
    entry['country'] = node.node_attrs.country.value;
  }

  // get clade if exists
  if (node.node_attrs.clade_membership) {
    entry['clade'] = node.node_attrs.clade_membership.value;
  } else if (node.branch_attrs && node.branch_attrs.labels && node.branch_attrs.labels.clade) {
    entry['clade'] = node.branch_attrs.labels.clade;
  }
  // get labs if exists
  if (node.node_attrs.originating_lab) {
    entry['originating_lab'] = node.node_attrs.originating_lab.value;
  }
  if (node.node_attrs.submitting_lab) {
    entry['submitting_lab'] = node.node_attrs.submitting_lab.value;
  }

  // sampling_date if exists
  if (node.node_attrs.num_date) {
    entry['sampling_date'] = node.node_attrs.num_date.value;
  }
  
  // get mutations if exists
  if (node.branch_attrs && node.branch_attrs.labels) {
    entry['mutations'] = node.branch_attrs.labels.aa;
  }
  // get nuc as string if exists
  if (node.branch_attrs && node.branch_attrs.mutations && node.branch_attrs.mutations.nuc) {
    entry['nuc'] = node.branch_attrs.mutations.nuc.join('; ');
  }

  // get genbank and gisaid if exists
  if (node.node_attrs.genbank_accession) {
    entry['genbank'] = node.node_attrs.genbank_accession.value;
  }
  if (node.node_attrs.gisaid_epi_isl) {
    entry['gisaid'] = node.node_attrs.gisaid_epi_isl.value;
  }

  rows.push(entry);

  // process children
  if (node.children && node.children.length > 0) {
    node.children.map(processTreeNode)
      .forEach(arr => {
        rows = rows.concat(arr);
      });
  }
}