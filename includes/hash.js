function hash_ordered_columns(ordered_list_of_column_names) {
    return `
        sha256(CONCAT(${ordered_list_of_column_names.map(column => `UPPER(CAST(${column} AS STRING))`).join(',')}))`;
  }

  module.exports = { hash_ordered_columns };